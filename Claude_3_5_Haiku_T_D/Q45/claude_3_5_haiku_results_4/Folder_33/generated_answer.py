def palindromes_between_indices(s):
    letters = [char.lower() for char in s[7:10] if char.isalpha()]
    palindromes = set()

    def generate_palindromes(current, remaining):
        if len(current) >= 4 and ''.join(current) == ''.join(current)[::-1]:
            palindromes.add(''.join(current))
        for i in range(len(remaining)):
            letter = remaining[i]
            new_current = current + [letter]
            new_remaining = remaining[:i] + remaining[i + 1:]
            generate_palindromes(new_current, new_remaining)
    generate_palindromes([], letters)
    return palindromes