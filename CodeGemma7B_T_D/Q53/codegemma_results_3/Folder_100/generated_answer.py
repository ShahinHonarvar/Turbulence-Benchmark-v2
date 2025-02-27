import collections

def palindrome_of_length_at_least_n(s):
    palindrome_set = set()
    temp = s.lower()
    temp = ''.join(temp.split())
    for i in range(len(temp)):
        for j in range(i + 47, len(temp)):
            sub_str = temp[i:j + 1]
            if sub_str == sub_str[::-1]:
                palindrome_set.add(s[i:j + 1])
    return palindrome_set