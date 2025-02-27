def palindromes_of_specific_lengths(s):
    s = s[17:96]
    return set([part[i:j] for i in range(len(part) - 49) for j in range(i + 13, len(part)) if part[i:j].lower() == part[i:j][::-1].lower() and part[i:j].isalpha()])