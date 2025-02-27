from collections import Counter

def palindromes_between_indices(text):
    """
            The function receives a text and returns a set of palindromes of length >= 5.
            """
    if text[6:10] == '':
        return set()
    letters = Counter(text[6:10].lower())
    count_letters = len(letters)
    min_base = ord('a')
    max_base = ord('z')
    ans = set()

    def backtrack(comb, end, start):
        if end - start + 1 >= 5:
            ans.add(''.join(comb))
        for c in range(start, end + 1):
            comb.append(chr(c))
            backtrack(comb, end, c + 1)
            comb.pop()
    backtrack([], max_base - count_letters + 1, min_base)
    return ans