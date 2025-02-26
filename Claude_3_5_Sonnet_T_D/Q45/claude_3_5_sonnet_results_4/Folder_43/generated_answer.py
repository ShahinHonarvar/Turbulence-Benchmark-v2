def palindromes_between_indices(s):
    letters = [c.lower() for c in s[2:6] if c.isalpha()]

    def generate_palindromes(chars, current='', left=0, right=0):
        if len(current) >= 4 and current == current[::-1]:
            palindromes.add(current)
        if left < len(chars):
            generate_palindromes(chars, chars[left] + current + chars[left], left + 1, right)
        if right < len(chars):
            generate_palindromes(chars, current + chars[right], left, right + 1)
    palindromes = set()
    generate_palindromes(letters)
    return palindromes