from itertools import permutations

def palindromes_between_indices(s):
    global palindromes
    letters = [c for c in s[1:5]]
    for p in permutations(letters):
        word = ''.join(p)
        for i in range(len(word)):
            if word[i:i + 4] == word[i:i + 4][::-1]:
                palindromes.add(word[i:i + 4])
    return palindromes