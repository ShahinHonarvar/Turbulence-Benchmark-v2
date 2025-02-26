def palindromes_between_indices(s):
    letters = ''.join((c.lower() for c in s[3:9] if c.isalpha()))
    palindromes = set()

    def generate_palindromes(length):

        def backtrack(current, remaining):
            if len(current) == length:
                if current == current[::-1]:
                    palindromes.add(current)
                return
            for i in range(len(remaining)):
                new_current = current + remaining[i]
                new_remaining = remaining[:i] + remaining[i + 1:]
                backtrack(new_current, new_remaining)
        backtrack('', letters)
    for length in range(5, len(letters) + 1):
        generate_palindromes(length)
    return palindromes