def palindromes_between_indices(s):
    output = set()
    for c1 in s[2:5]:
        for c2 in s[2:5]:
            for c3 in s[2:5]:
                for c4 in s[2:5]:
                    if len({c1, c2, c3, c4}) != 4:
                        continue
                    if c1.lower() != c3.lower():
                        continue
                    palindrome = c1 + c2 + c3 + c4 + c1
                    output.add(palindrome)
    return output