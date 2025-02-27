def palindromes_between_indices(text):
    text = text.lower()
    if not text[6:10]:
        return set()

    def is_palindrome(word):
        return word == word[::-1]

    def get_permutations(text):
        if not text:
            return ['']
        result = []
        for i in range(len(text)):
            for perm in get_permutations(text[:i] + text[i + 1:]):
                result.append(text[i] + perm)
        return result
    permutations = get_permutations(text[6:10])
    return {p for p in permutations if is_palindrome(p) and len(p) >= 5}