def palindromes_between_indices(string):
    letters = [char.lower() for char in string[6:10] if char.isalpha()]

    def generate_palindromes(letters):

        def backtrack(current, remaining):
            if len(current) >= 3 and len(remaining) == 0:
                return {current if len(current) % 2 == 0 else current[:-1]}
            palindromes = set()
            for i in range(len(remaining)):
                new_current = current + remaining[i]
                new_remaining = remaining[:i] + remaining[i + 1:]
                if len(new_current) % 2 == 0 and new_current == new_current[::-1]:
                    palindromes.add(new_current)
                palindromes.update(backtrack(new_current, new_remaining))
            return palindromes
        return backtrack('', letters)
    return generate_palindromes(letters)