def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[3:8]))
    letters = letters.lower()
    palindromes = set()

    def is_palindrome(word):
        return word == word[::-1]

    def generate_palindromes(left, right, current):
        if len(current) >= 5 and is_palindrome(current):
            palindromes.add(current)
        if left < right:
            generate_palindromes(left + 1, right, current + letters[left])
            generate_palindromes(left, right - 1, current + letters[right - 1])
    generate_palindromes(0, len(letters), '')
    return palindromes