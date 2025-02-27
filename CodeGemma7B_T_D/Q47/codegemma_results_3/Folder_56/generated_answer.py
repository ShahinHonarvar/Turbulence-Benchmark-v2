from string import ascii_lowercase

def palindromes_of_specific_lengths(word):
    ans = set()
    for i in range(1, 9):
        for j in range(i + 3, 8):
            for k in range(i, j + 1):
                ans |= {word[j:k][::-1] + word[i:j]}
    ans &= {p for p in ans if p.lower() == p}
    return ans