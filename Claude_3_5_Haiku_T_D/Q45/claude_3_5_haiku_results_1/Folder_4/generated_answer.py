def palindromes_between_indices(s):
    letters = [char.lower() for char in s[3:10] if char.isalpha()]

    def generate_palindromes(letters):

        def backtrack(current, remaining):
            if len(current) >= 7 and len(current) % 2 == 1:
                mid = len(current) // 2
                if current[:mid] == current[mid + 1:][::-1]:
                    result.add(current)
            for i in range(len(remaining)):
                if i > 0 and remaining[i] == remaining[i - 1]:
                    continue
                backtrack(current + remaining[i], remaining[:i] + remaining[i + 1:])
        result = set()
        letters.sort()
        backtrack('', letters)
        return result
    return generate_palindromes(letters)