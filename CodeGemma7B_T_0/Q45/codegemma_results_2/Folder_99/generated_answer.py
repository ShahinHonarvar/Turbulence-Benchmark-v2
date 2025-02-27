def palindromes_between_indices(text):
    text = text.lower()
    palindromes = set()
    for i in range(4, 9):
        for j in range(i + 1, 9):
            for k in range(j + 1, 9):
                for l in range(k + 1, 9):
                    for m in range(l + 1, 9):
                        for n in range(m + 1, 9):
                            if text[i] in 'abcdefghijklmnopqrstuvwxyz' and text[j] in 'abcdefghijklmnopqrstuvwxyz' and (text[k] in 'abcdefghijklmnopqrstuvwxyz') and (text[l] in 'abcdefghijklmnopqrstuvwxyz') and (text[m] in 'abcdefghijklmnopqrstuvwxyz') and (text[n] in 'abcdefghijklmnopqrstuvwxyz'):
                                palindrome = text[i] + text[j] + text[k] + text[l] + text[m] + text[n]
                                palindromes.add(palindrome)
    return palindromes