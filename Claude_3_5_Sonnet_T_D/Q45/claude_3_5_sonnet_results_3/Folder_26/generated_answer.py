def palindromes_between_indices(s):
    letters = [c.lower() for c in s[4:7] if c.isalpha()]
    if len(letters) < 2:
        return set()

    def generate_palindromes(chars, current='', used=0):
        if len(current) >= 3 and current == current[::-1]:
            palindromes.add(current)
        for i, char in enumerate(chars):
            if not used & 1 << i:
                generate_palindromes(chars, current + char, used | 1 << i)
                generate_palindromes(chars, char + current, used | 1 << i)
    palindromes = set()
    generate_palindromes(letters)
    return palindromes