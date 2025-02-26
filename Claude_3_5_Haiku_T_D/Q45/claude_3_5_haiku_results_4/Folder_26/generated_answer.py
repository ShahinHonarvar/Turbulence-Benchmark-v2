def palindromes_between_indices(s):
    segment = s[4:7].lower()
    letters = [char for char in segment if char.isalpha()]

    def generate_palindromes(chars):

        def backtrack(current, remaining):
            if len(current) >= 3 and len(current) == len(remaining) * 2 - (1 if len(remaining) % 2 else 0):
                return {current}
            result = set()
            for i in range(len(remaining)):
                if i > 0 and remaining[i] == remaining[i - 1]:
                    continue
                new_current = current + remaining[i]
                new_remaining = remaining[:i] + remaining[i + 1:]
                result.update(backtrack(new_current, new_remaining))
                if len(new_current) >= 3 and len(new_current) % 2 == 1:
                    reversed_prefix = new_current[:len(new_current) // 2]
                    new_palindrome = new_current + reversed_prefix[::-1]
                    if len(new_palindrome) >= 3:
                        result.add(new_palindrome)
            return result
        return backtrack('', chars)
    return generate_palindromes(sorted(letters))