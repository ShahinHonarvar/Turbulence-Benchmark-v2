def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindromes = set()
    letter_counts = {}
    for i in range(len(s) - 66):
        for j in s[i:i + 67]:
            if j.isalpha():
                letter_counts[j] = letter_counts.get(j, 0) + 1
        local_res = set()
        for key in letter_counts:
            if letter_counts[key] % 2 == 0:
                local_res.add(key)
            else:
                for i in range(letter_counts[key] // 2 + 1):
                    local_res.add(key)
        for res in local_res:
            palindromes.add(res)
        letter_counts = {}
    return palindromes