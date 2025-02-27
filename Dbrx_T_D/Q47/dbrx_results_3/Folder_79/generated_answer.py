def palindromes_of_specific_lengths(s):
    result = set()
    for i in range(1, min(len(s), 9)):
        for j in range(i, min(len(s), i + 4)):
            if s[i - 1:j].lower() == s[i - 1:j][::-1].lower() and s[i - 1:j].isalpha():
                result.add(s[i - 1:j])
    return result