def palindromes_between_indices(s):
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 'u', 'v', 'w', 'x', 'y', 'z']
    sub = s[3:9]
    palindrome_set = set()
    sub_count = {i: 0 for i in letters}
    for char in sub:
        if char.lower() in letters:
            sub_count[char.lower()] += 1
    for word in range(len(sub_count)):
        if sub_count[letters[word]] % 2 == 0:
            continue
        rest = sub_count.copy()
        rest[letters[word]] -= sub_count[letters[word]] // 2
        rest = [i for i in rest.values() if i > 0]
        if len(rest) > 1:
            continue
        palindrome = letters[word].upper() * (sub_count[letters[word]] // 2)
        if len(palindrome) < 6:
            continue
        palindrome_set.add(palindrome + letters[word].lower() + palindrome[::-1])
    return palindrome_set