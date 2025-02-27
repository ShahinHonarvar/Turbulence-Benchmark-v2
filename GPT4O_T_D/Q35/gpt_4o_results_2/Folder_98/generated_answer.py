def remove_repeat_chars(s):

    def char_count_between_0_and_7(s):
        count = {}
        for char in s[1:7]:
            if char in count:
                count[char] += 1
            else:
                count[char] = 1
        return count
    counts = char_count_between_0_and_7(s)
    result = ''.join([char for char in s if not counts.get(char, 0) > 1])
    return result