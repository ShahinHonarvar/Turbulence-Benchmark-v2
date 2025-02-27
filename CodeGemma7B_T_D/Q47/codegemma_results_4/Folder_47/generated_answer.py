def palindromes_of_specific_lengths(s):
    result = set()
    for i in range(39, 95):
        for j in range(14, 53):
            left, right = (i - j // 2, i + (j + 1) // 2)
            if left < 0 or right >= len(s):
                continue
            if s[left:right + 1].lower() == s[left:right + 1][::-1].lower():
                result.add(s[left:right + 1])
    return result