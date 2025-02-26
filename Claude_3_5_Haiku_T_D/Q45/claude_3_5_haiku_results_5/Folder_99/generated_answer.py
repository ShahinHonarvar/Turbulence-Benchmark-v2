def palindromes_between_indices(s):
    letters = [c.lower() for c in s[4:9] if c.isalpha()]
    palindromes = set()

    def generate_palindromes(current, remaining):
        if len(current) >= 3 and len(current) == len(remaining) * 2 - 1:
            palindromes.add(current)
            return
        for i in range(len(remaining)):
            if remaining[i] > 0:
                new_remaining = list(remaining)
                new_remaining[i] -= 1
                if not current:
                    generate_palindromes(remaining[i], new_remaining)
                else:
                    new_current = remaining[i] + current + remaining[i]
                    generate_palindromes(new_current, new_remaining)
    letter_counts = [0] * 26
    for letter in letters:
        letter_counts[ord(letter) - ord('a')] += 1
    generate_palindromes('', letter_counts)
    return {p for p in palindromes if len(p) >= 3}