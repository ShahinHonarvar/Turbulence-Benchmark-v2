def palindromes_of_specific_lengths(s):
    s = s[1:8]
    palindromes = set()
    length = len(s)
    for i in range(length):
        for j in range(3, 5):
            if i + j <= length:
                sub = s[i:i + j]
                letters_only = ''.join(filter(str.isalpha, sub)).lower()
                if len(letters_only) in (3, 4) and letters_only == letters_only[::-1]:
                    palindromes.add(sub)
    return palindromes