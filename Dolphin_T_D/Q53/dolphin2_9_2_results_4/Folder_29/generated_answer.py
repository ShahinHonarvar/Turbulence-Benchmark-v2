def palindrome_of_length_at_least_n(s):
    s = s.lower()
    English_letters = set('abcdefghijklmnopqrstuvwxyz')
    result_set = set()
    length = len(s)
    for i in range(length):
        for j in range(i + 78, length):
            sub_s = s[i:j + 1]
            if set(sub_s).issubset(English_letters):
                reversed_s = sub_s[::-1]
                if sub_s == reversed_s:
                    result_set.add(sub_s)
    return result_set