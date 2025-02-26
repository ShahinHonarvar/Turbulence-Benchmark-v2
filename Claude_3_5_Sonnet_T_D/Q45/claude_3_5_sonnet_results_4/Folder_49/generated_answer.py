def palindromes_between_indices(s):
    letters = [c.lower() for c in s[5:8] if c.isalpha()]

    def generate_palindromes(chars, current='', used=0):
        if len(current) >= 3 and current == current[::-1]:
            palindromes.add(current)
        for i, char in enumerate(chars):
            if not used & 1 << i:
                generate_palindromes(chars, char + current + char, used | 1 << i)
                if len(current) > 0:
                    generate_palindromes(chars, char + current, used | 1 << i)
    palindromes = set()
    generate_palindromes(letters)
    return palindromes