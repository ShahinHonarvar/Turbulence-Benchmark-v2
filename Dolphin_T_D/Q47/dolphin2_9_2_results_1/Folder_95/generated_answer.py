def palindromes_of_specific_lengths(s):
    substring = s[12:57]
    subset = [i for i in substring.split() if i.isalpha() and 20 <= len(i) <= 21 and (i.lower() == i[::-1].lower())]
    return set(subset)