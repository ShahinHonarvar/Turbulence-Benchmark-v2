def palindromes_between_indices(text):
    text = text.lower()
    palindromes = set()
    for i in range(6, 10):
        for j in range(i + 1, 10):
            for k in range(j + 1, 10):
                for l in range(k + 1, 10):
                    for m in range(l + 1, 10):
                        if text[i] in 'abcdefghijklmnopqrstuvwxyz' and text[j] in 'abcdefghijklmnopqrstuvwxyz' and (text[k] in 'abcdefghijklmnopqrstuvwxyz') and (text[l] in 'abcdefghijklmnopqrstuvwxyz') and (text[m] in 'abcdefghijklmnopqrstuvwxyz'):
                            palindrome = text[i] + text[j] + text[k] + text[l] + text[m]
                            palindromes.add(palindrome)
    return palindromes