import re

def palindrome_of_length_at_least_n(txt):
    all_found = []
    for i in re.findall('[a-zA-Z]{112,}', txt):
        i = i.lower()
        a = i
        b = i[::-1]
        if a == b:
            all_found.append(i)
        if a != b:
            a = list(a)
            for k in range(26):
                a.insert(k, chr(ord('a') + k))
                b = a[::-1]
                if a == b:
                    all_found.append(''.join(a))
                a.pop(k)
    return set(all_found)