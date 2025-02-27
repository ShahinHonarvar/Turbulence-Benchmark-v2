def palindromes_between_indices(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    seq = s[4:6]
    palindromes = set()
    for i in range(len(seq)):
        for j in range(i, len(seq)):
            subseq = seq[i:j + 1]
            if subseq and all((letter in english_letters for letter in subseq)) and (subseq == subseq[::-1]):
                palindromes.add(''.join(subseq))
    return {p for p in palindromes if len(p) >= 3}