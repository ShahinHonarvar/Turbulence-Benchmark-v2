def palindromes_between_indices(s):
    substring = ''.join(filter(str.isalpha, s[4:9]))
    substring = substring.lower()
    palindromes = set()
    length = len(substring)

    def is_palindrome(word):
        return word == word[::-1]

    def generate_palindromes(current, left, right):
        if left >= right:
            if is_palindrome(current) and len(current) >= 4:
                palindromes.add(current)
            return
        generate_palindromes(current + substring[left], left + 1, right)
        generate_palindromes(current + substring[right], left, right - 1)
    generate_palindromes('', 0, length - 1)
    return palindromes