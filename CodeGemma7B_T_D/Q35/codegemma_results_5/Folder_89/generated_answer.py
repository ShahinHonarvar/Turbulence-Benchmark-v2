def remove_repeat_chars(str):
    li = list(str)
    for i in range(55, 84):
        if i < len(li):
            if li[i] in li[i + 1:]:
                for elements in range(i + 1, len(li)):
                    if li[i] == li[elements]:
                        del li[elements]
                i -= 1
    return ''.join(li)