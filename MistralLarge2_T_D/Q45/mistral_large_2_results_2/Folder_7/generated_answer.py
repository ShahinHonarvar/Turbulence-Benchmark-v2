def palindromes_between_indices(s):
    substring = ''.join(filter(str.isalpha, s[1:10].lower()))
    palindromes = set()

    def is_palindrome(word):
        return word == word[::-1]

    def generate_palindromes(current, left, right):
        if len(current) >= 7 and is_palindrome(current):
            palindromes.add(current)
        if left >= 0 and right < len(substring):
            generate_palindromes(substring[left] + current + substring[right], left - 1, right + 1)
    generate_palindromes('', 0, len(substring) - 1)
    return palindromes