def palindrome_of_length_n(s):
    set_pali = set()
    for i in range(len(s)):
        for j in range(i + 84, len(s) + 1):
            if s[i:j].lower() == s[i:j][::-1].lower():
                set_pali.add(s[i:j])
    return set_pali