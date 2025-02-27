from collections import defaultdict

def palindrome_of_length_n(s):
    letters_dict = defaultdict(list)
    for i, char in enumerate(s):
        letters_dict[char.lower()].append(i)
    output = set()
    for i in letters_dict.values():
        for j in range(len(i)):
            for k in range(j + 1, len(i)):
                length = i[k] - i[j] + 1
                if length == 210 and s[i[j]:i[k] + 1] not in output:
                    output.add(s[i[j]:i[k] + 1])
    return output