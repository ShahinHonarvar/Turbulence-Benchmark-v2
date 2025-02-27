def palindromes_between_indices(text):
    alphabetized = sorted(map(str.lower, text[2:7]))
    length = len(alphabetized)
    if length < 4:
        return set()
    seen = set()
    for i in range(length):
        for j in range(i, length):
            Palindrome = ''.join(alphabetized[i:j + 1])
            seen.add(Palindrome)
    return seen