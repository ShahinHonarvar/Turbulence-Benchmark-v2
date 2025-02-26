def palindromes_between_indices(s):
    letters = set((c.lower() for c in s[2:5] if c.isalpha()))
    palindromes = set()

    def generate_palindromes(current, remaining):
        if len(current) >= 3:
            palindrome = current + current[-2::-1]
            palindromes.add(palindrome)
        if len(current) < 3:
            for char in remaining:
                new_remaining = remaining.copy()
                new_remaining.remove(char)
                generate_palindromes(current + char, new_remaining)
    generate_palindromes('', letters)
    return palindromes