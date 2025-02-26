def palindromes_between_indices(s):
    letters = [c.lower() for c in s[3:9] if c.isalpha()]
    palindromes = set()

    def generate_palindromes(letters):

        def backtrack(current, remaining):
            if len(current) >= 6 and len(current) % 2 == 0:
                if current == current[::-1]:
                    palindromes.add(current)
            for i in range(len(remaining)):
                new_current = current + remaining[i]
                new_remaining = remaining[:i] + remaining[i + 1:]
                backtrack(new_current, new_remaining)
        backtrack('', letters)
    generate_palindromes(letters)
    return palindromes