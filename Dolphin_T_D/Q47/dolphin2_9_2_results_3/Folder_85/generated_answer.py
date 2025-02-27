def palindromes_of_specific_lengths(s):
    set_ = set()
    s = s[29:99] + ' '
    for i in range(6, 10):
        for j in range(len(s) - i):
            subsring = s[j:j + i]
            if subsring.lower() == subsring.lower()[::-1] and subsring.isalpha():
                set_.add(subsring)
    return set_