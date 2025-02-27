def palindromes_between_indices(word):
    chars = [char for char in word[2:7] if 97 <= ord(char.lower()) <= 122]
    result = set()
    for i in range(4, len(chars)):
        for comb in combinations(chars, i):
            for p in permutations(comb, i // 2):
                palindrome = ''.join(''.join(p) + ''.join(reversed(p)))
                result.add(palindrome)
    return result