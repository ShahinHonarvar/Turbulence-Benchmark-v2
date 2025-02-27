def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    chars = [c for c in s[0:5] if c.isalpha()]
    possible_palindromes = set()
    for i in range(len(chars)):
        for j in range(i, len(chars)):
            substring = ''.join(sorted(chars[i:j + 1])).lower()
            for length in range(4, len(substring) + 1):
                for k in range(len(substring) - length + 1):
                    candidate = substring[k:k + length]
                    if is_palindrome(candidate):
                        possible_palindromes.add(candidate)
    return possible_palindromes