def palindromes_between_indices(s):
    s = s[2:6].lower()
    letters = [c for c in s if c.isalpha()]
    palindromes = set()

    def is_palindrome(word):
        return word == word[::-1]

    def generate_palindromes(letters, current='', left=0, right=0):
        if len(current) > 3 and is_palindrome(current):
            palindromes.add(current)
        if left < len(letters):
            generate_palindromes(letters, letters[left] + current, left + 1, right)
        if right < len(letters):
            generate_palindromes(letters, current + letters[right], left, right + 1)
    generate_palindromes(letters)
    return palindromes