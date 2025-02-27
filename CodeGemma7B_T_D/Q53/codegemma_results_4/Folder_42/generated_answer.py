def palindrome_of_length_at_least_n(text):

    def is_palindrome(candidate):
        return candidate == candidate[::-1]

    def find_candidates(text):
        candidates = set()
        for i in range(len(text) - 44):
            for j in range(i + 44, len(text)):
                candidate = text[i:j + 1]
                if is_palindrome(candidate):
                    candidates.add(candidate)
        return candidates
    candidates = find_candidates(text)
    candidates = {candidate.lower() for candidate in candidates}
    return candidates