def palindromes_of_specific_lengths(s):
    s = s[15:87]
    the_palindromes = set()
    for length in range(51, 61):
        for i in range(len(s)):
            curr = ''
            for j in range(i, i + length):
                if j < len(s) and s[j].isalpha():
                    curr += s[j].lower()
                else:
                    break
            if curr == curr[::-1]:
                the_palindromes.add(curr)
    return the_palindromes