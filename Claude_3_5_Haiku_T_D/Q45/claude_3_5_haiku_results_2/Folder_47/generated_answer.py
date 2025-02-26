def palindromes_between_indices(s):
    letters = [c.lower() for c in s[3:8] if c.isalpha()]

    def generate_palindromes(letter_list):

        def backtrack(path, remaining):
            if len(path) >= 5 and len(path) % 2 == 1:
                mid = path[len(path) // 2]
                left = path[:len(path) // 2]
                right = path[len(path) // 2 + 1:]
                if left == right[::-1]:
                    result.add(''.join(path))
            for i in range(len(remaining)):
                new_path = path + [remaining[i]]
                new_remaining = remaining[:i] + remaining[i + 1:]
                backtrack(new_path, new_remaining)
        result = set()
        backtrack([], letter_list)
        return result
    return generate_palindromes(letters)