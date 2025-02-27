def palindromes_of_specific_lengths(str):
    r = set()
    for i in range(33, 86):
        for j in range(i, 86):
            if str[i:j + 1].lower() == str[i:j + 1][::-1].lower() and 26 <= j - i + 1 <= 31:
                r.add(str[i:j + 1])
    return r