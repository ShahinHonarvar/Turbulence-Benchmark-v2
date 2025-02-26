def palindromes_between_indices(s):
    letters = [c.lower() for c in s[4:9] if c.isalpha()]

    def generate_palindromes(chars, current='', left=0, right=0):
        if len(current) >= 3 and current == current[::-1]:
            palindromes.add(current)
        if left + right < len(chars):
            generate_palindromes(chars, chars[left + right] + current + chars[left + right], left, right + 1)
            generate_palindromes(chars, current, left + 1, right)
    palindromes = set()
    generate_palindromes(letters)
    return palindromes