def palindrome_of_length_n(s):
    s = s.lower()
    result = set()
    for i in range(len(s) - 19):
        if s[i:i + 20] == s[i:i + 20][::-1] and set(s[i:i + 20]) <= {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'}:
            result.add(s[i:i + 20])
    return result