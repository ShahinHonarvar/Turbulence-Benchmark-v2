from collections import Counter

def palindromes_between_indices(string):
    letters = Counter((string[i].lower() for i in range(7) if string[i].isalpha()))
    size = sum(letters.values())
    if size < 7:
        return set()

    def generate(combination, count, size):
        if len(combination) == size // 2:
            yield ''.join(combination)
            return
        if size % 2 == 0 and len(combination) == size // 2 - 1:
            for letter in count:
                if count[letter] >= 2:
                    yield from generate(combination + [letter, letter], {**count, letter: count[letter] - 2}, size)
            return
        for letter in count:
            if count[letter] > 0:
                yield from generate(combination + [letter], {**count, letter: count[letter] - 1}, size)
    palindromes = set()
    for combination in generate([], letters, size):
        palindrome = ''.join(combination)
        palindromes.add(palindrome + (palindrome if size % 2 == 0 else palindrome[:-1])[::-1])
    return palindromes