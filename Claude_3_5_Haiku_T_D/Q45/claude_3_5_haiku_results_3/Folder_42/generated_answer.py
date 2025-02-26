def palindromes_between_indices(s):
    letters = [char.lower() for char in s[6:10] if char.isalpha()]

    def generate_palindromes(chars):

        def backtrack(current, remaining):
            if len(current) >= 3 and len(current) % 2 == 1:
                mid = len(current) // 2
                if current == current[:mid] + current[mid] + current[mid::-1]:
                    results.add(current)
            for i in range(len(remaining)):
                if i > 0 and remaining[i] == remaining[i - 1]:
                    continue
                backtrack(current + remaining[i], remaining[:i] + remaining[i + 1:])
        results = set()
        chars.sort()
        backtrack('', chars)
        return results
    return generate_palindromes(letters)