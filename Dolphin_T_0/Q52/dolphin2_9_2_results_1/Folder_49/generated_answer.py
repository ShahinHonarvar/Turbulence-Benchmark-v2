def palindrome_of_length_n(s):
    result = set()
    s = s.lower()
    letter_count = {}
    for c in s:
        if c.isalpha():
            if c in letter_count:
                letter_count[c] += 1
            else:
                letter_count[c] = 1
    for key in letter_count:
        if letter_count[key] > 47 / 2:
            return result
    for i in range(len(s) - 46):
        substring = s[i:i + 47]
        if substring == substring[::-1]:
            result.add(substring)
    return result