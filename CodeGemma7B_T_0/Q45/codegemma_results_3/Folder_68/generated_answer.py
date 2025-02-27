def palindromes_between_indices(text):
    text = text.lower()
    if not text or len(text) < 4 or (not text[1:9].isalpha()):
        return set()

    def is_palindrome(word):
        return word == word[::-1]

    def generate_permutations(text):
        if not text:
            return ['']
        result = []
        for i in range(len(text)):
            for perm in generate_permutations(text[:i] + text[i + 1:]):
                result.append(text[i] + perm)
        return result
    permutations = generate_permutations(text[1:9])
    palindromes = {word for word in permutations if is_palindrome(word)}
    return palindromes