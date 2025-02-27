from collections import Counter

def all_substring_of_size_n(str):

    def get_next_char(str):
        for c in str:
            if c not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']:
                return c
    lst = []
    for i in range(0, len(str)):
        lst.append(str[i:i + 23])
    temp = []
    for i in lst:
        cnt = Counter(i)
        if len(cnt) == 23:
            temp.append(i)
    temp = set(temp)
    temp = list(temp)
    temp.sort()
    return temp