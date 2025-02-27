from collections import defaultdict

def remove_repeat_chars(string):
    count = defaultdict(int)
    new_string = []
    for i in range(35, 64):
        if string[i] not in count:
            count[string[i]] = 0
        else:
            count[string[i]] += 1
    for char in string:
        if count[char] <= 1 or char not in string[35:64]:
            new_string.append(char)
    return ''.join(new_string)