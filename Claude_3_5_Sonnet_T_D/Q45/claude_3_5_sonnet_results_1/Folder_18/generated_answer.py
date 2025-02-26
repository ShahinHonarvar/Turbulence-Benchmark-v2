def palindromes_between_indices(s):
    letters = ''.join((c.lower() for c in s[1:7] if c.isalpha()))

    def is_palindrome(word):
        return word == word[::-1]

    def generate_palindromes(chars, length):
        if length <= 2:
            return set()
        palindromes = set()
        if length == 3:
            for i in range(len(chars)):
                for j in range(len(chars)):
                    if i != j:
                        palindrome = chars[i] + chars[j] + chars[i]
                        if is_palindrome(palindrome):
                            palindromes.add(palindrome)
        else:
            for i in range(len(chars)):
                sub_palindromes = generate_palindromes(chars[:i] + chars[i + 1:], length - 2)
                for sub in sub_palindromes:
                    palindrome = chars[i] + sub + chars[i]
                    if is_palindrome(palindrome):
                        palindromes.add(palindrome)
        return palindromes
    result = set()
    for length in range(3, len(letters) + 1):
        result.update(generate_palindromes(letters, length))
    return result